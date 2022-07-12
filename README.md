<!--
SPDX-FileCopyrightText: Copyright 2004-present Facebook. All Rights Reserved.
SPDX-FileCopyrightText: 2019-present Open Networking Foundation <info@opennetworking.org>

SPDX-License-Identifier: Apache-2.0
-->
# fb-kpimon-xapp
key performance indicator app

This app subscribes to the kpm (key performance metrics) service model and send control request to e2 node


## Make image

You can build the image of `fb-kpimon-xapp` using make:
```
make image
```

## Deploy container

You can deploy the `fb-kpimon-xapp` image using helm:
```
helm install -n riab fb-kpimon-xapp fb-kpimon-xapp
```

uninstall:
```
helm uninstall -n riab fb-kpimon-xapp
```

view logs:
```
kubectl logs --namespace=riab --tail=100 -lname=fb-kpimon-xapp -c fb-kpimon-xapp -f
```
