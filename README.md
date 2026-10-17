# bi-robotics-plugins

Built plugin bundles of [BI-Robotics](https://github.com/magerdaniel) for BI tools, served by
[jsDelivr](https://www.jsdelivr.com/) -- always pinned to a commit:

    https://cdn.jsdelivr.net/gh/magerdaniel/bi-robotics-plugins@<commit>/<path>

This repository holds **built files only, no data**. The sources live in the (private) BI-Robotics repository and
are written there by code; a deploy step copies the build here.

| Path | What | Source |
|---|---|---|
| `gooddata/chartkitchen/dp_bir_chartkitchen.mjs` | GoodData dashboard plugin: draws every visualization that carries `properties.chartkitchen` through the unchanged ChartKitchen bundle | `plugins/gooddata-chartkitchen` |

## Third-party code in the bundles

- **ChartKitchen byDatenWG** 1.47.0.0, unchanged -- (c) 2026 Michael Tenner / DatenWG, MIT licence
  ([LICENSE-ChartKitchen](LICENSE-ChartKitchen)), source:
  [Losveratos/Power-BI-Custom-Visuals-byDatenWG](https://github.com/Losveratos/Power-BI-Custom-Visuals-byDatenWG).
- **GoodData.UI** libraries, as built by the GoodData plugin toolkit (shared with the dashboard at runtime) --
  (c) GoodData Corporation, under their licences.
