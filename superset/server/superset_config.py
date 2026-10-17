# Superset configuration of the BI-Robotics server (217.154.213.84), mounted into the container at
# /app/pythonpath/superset_config.py -- Superset reads it on start (scripts/superset/SERVER_CHANGE.md).
# After a change: docker compose restart superset (up -d does not pick up a changed mounted file).
#
# DRILL_TO_DETAIL off (#53, decided 2026-10-14): every dashboard here runs on Cube, and Cube's SQL API refuses the
# ungrouped rows "Drill to detail" asks for ("must appear in the GROUP BY clause") -- the menu item only ever fails.
# Superset 6.1 still reads the flag (deprecated, default True); when a later version removes it, the item comes back.
#
# DYNAMIC_PLUGINS on (#57, 2026-10-17): Superset loads a chart plugin from a URL without a frontend build -- the
# ChartKitchen plugin from jsDelivr (bi-robotics-plugins), registered under Manage > Plugins.
FEATURE_FLAGS = {
    "DRILL_TO_DETAIL": False,
    "DYNAMIC_PLUGINS": True,
}

# The plugin list for Superset's own loader (#57, option 2, decided 2026-10-17). The browser asks
# /dynamic-plugins/api/read which plugins are registered (superset-frontend DynamicPluginProvider); that route was
# Flask-AppBuilder 4's legacy JSON API, removed in Flask-AppBuilder 5 (Superset 6.1 pins 5.2.3) -- without it no
# dynamic plugin loads and dashboards may wait for it (apache/superset#36211). This gives it back: read-only, logged-in
# users only, the rows of Superset's own table. Remove it when Superset ships the route again or drops the loader.
from flask import Blueprint, jsonify
from flask_login import current_user

_dynamic_plugins = Blueprint("bir_dynamic_plugins_read", __name__)


@_dynamic_plugins.route("/dynamic-plugins/api/read")
def _dynamic_plugins_read():
    if not current_user.is_authenticated:
        return jsonify(message="Not authenticated"), 401
    from superset.extensions import db
    from superset.models.dynamic_plugins import DynamicPlugin

    rows = db.session.query(DynamicPlugin).order_by(DynamicPlugin.id).all()
    result = [{"id": p.id, "name": p.name, "key": p.key, "bundle_url": p.bundle_url} for p in rows]
    return jsonify(result=result, count=len(result))


BLUEPRINTS = [_dynamic_plugins]
