# demo-web

![Version: 0.1.12](https://img.shields.io/badge/Version-0.1.12-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.16.0](https://img.shields.io/badge/AppVersion-1.16.0-informational?style=flat-square)

A Helm chart for Kubernetes

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| automountServiceAccountToken | bool | `false` |  |
| autoscaling.enabled | bool | `false` |  |
| autoscaling.maxReplicas | int | `5` |  |
| autoscaling.minReplicas | int | `2` |  |
| autoscaling.scaleDownPolicies[0].periodSeconds | int | `60` |  |
| autoscaling.scaleDownPolicies[0].type | string | `"Pods"` |  |
| autoscaling.scaleDownPolicies[0].value | int | `2` |  |
| autoscaling.scaleDownPolicies[1].periodSeconds | int | `60` |  |
| autoscaling.scaleDownPolicies[1].type | string | `"Percent"` |  |
| autoscaling.scaleDownPolicies[1].value | int | `50` |  |
| autoscaling.scaleUpPolicies[0].periodSeconds | int | `60` |  |
| autoscaling.scaleUpPolicies[0].type | string | `"Pods"` |  |
| autoscaling.scaleUpPolicies[0].value | int | `1` |  |
| autoscaling.targetMemoryUtilizationPercentage | int | `150` |  |
| containerSecurityContext | object | `{"allowPrivilegeEscalation":false,"capabilities":{"add":["CHOWN"],"drop":["ALL","NET_RAW"]},"enabled":false,"seccompProfile":{"type":"RuntimeDefault"}}` | Toggle and define Back container-level security context |
| deployAnnotations | object | `{}` |  |
| deploymentStrategy | object | `{}` |  |
| fullnameOverride | string | `""` |  |
| gatewayApi.annotations | object | `{}` |  |
| gatewayApi.enabled | bool | `false` |  |
| gatewayApi.gateway.name | string | `""` |  |
| gatewayApi.gateway.namespace | string | `""` |  |
| gatewayApi.gateway.section | string | `""` |  |
| gatewayApi.httpRoute.hosts[0] | string | `"example.com"` |  |
| gatewayApi.httpRoute.path | string | `"/"` |  |
| gatewayApi.httpRoute.pathType | string | `"PathPrefix"` |  |
| global | object | `{"deployAnnotations":{},"deploymentStrategy":{},"image":{"imagePullPolicy":"","registry":""},"imagePullSecrets":"","nodeSelector":{},"podLabels":{},"priorityClassName":"","revisionHistoryLimit":10,"stakater":{"auto":false,"enabled":false},"tolerations":[]}` | values shared globally between chart and subcharts (use this part is you include subchart which need information from the parent chart)  |
| global.deployAnnotations | object | `{}` | Annotations for the all deployed Deployments |
| global.deploymentStrategy | object | `{}` | Deployment strategy for the all deployed Deployments |
| global.image | object | `{"imagePullPolicy":"","registry":""}` | set global image parameters |
| global.image.imagePullPolicy | string | `""` | set global image pullPolicy |
| global.image.registry | string | `""` | set global image registry |
| global.nodeSelector | object | `{}` | Default node selector for all components |
| global.podLabels | object | `{}` | Labels for all pods |
| global.priorityClassName | string | `""` | Default priority class for all components |
| global.revisionHistoryLimit | int | `10` | set global revision history limit |
| global.stakater | object | `{"auto":false,"enabled":false}` | the global configuration of the usage of Stakater reloader |
| global.stakater.auto | bool | `false` | enabled auto mode |
| global.stakater.enabled | bool | `false` | enabled stakater usage |
| global.tolerations | list | `[]` | Default tolerations for all components |
| image.digest | string | `""` |  |
| image.pullPolicy | string | `"Always"` |  |
| image.registry | string | `"docker.io"` |  |
| image.repository | string | `"ixxel/demo-web"` |  |
| image.tag | string | `"latest"` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations | object | `{}` |  |
| ingress.className | string | `"nginx"` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| ingress.tls | list | `[]` |  |
| livenessProbe.enabled | bool | `false` |  |
| livenessProbe.failureThreshold | int | `3` |  |
| livenessProbe.initialDelaySeconds | int | `0` |  |
| livenessProbe.path | string | `"/management/health/liveness"` |  |
| livenessProbe.periodSeconds | int | `10` |  |
| livenessProbe.timeoutSeconds | int | `1` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext.enabled | bool | `false` |  |
| podSecurityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| readinessProbe.enabled | bool | `false` |  |
| readinessProbe.failureThreshold | int | `3` |  |
| readinessProbe.initialDelaySeconds | int | `0` |  |
| readinessProbe.path | string | `"/management/health/readiness"` |  |
| readinessProbe.periodSeconds | int | `10` |  |
| readinessProbe.successThreshold | int | `1` |  |
| readinessProbe.timeoutSeconds | int | `5` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| rollouts.enabled | bool | `false` |  |
| rollouts.workloadRef.scaleDown | string | `"progressively"` |  |
| service.annotations | object | `{}` |  |
| service.externalIPs | list | `[]` |  |
| service.externalTrafficPolicy | string | `""` |  |
| service.labels | object | `{}` |  |
| service.loadBalancerIP | string | `""` |  |
| service.loadBalancerSourceRanges | list | `[]` |  |
| service.nodePort | int | `30080` |  |
| service.port | int | `80` |  |
| service.servicePortName | string | `"http"` |  |
| service.sessionAffinity | string | `""` |  |
| service.targetPort | int | `8080` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount | object | `{"annotations":{},"create":true,"labels":{},"name":""}` | the name of the service account used to access the API server |
| startupProbe.enabled | bool | `false` |  |
| startupProbe.failureThreshold | int | `20` |  |
| startupProbe.initialDelaySeconds | int | `0` |  |
| startupProbe.path | string | `"/management/health/liveness"` |  |
| startupProbe.periodSeconds | int | `3` |  |
| startupProbe.timeoutSeconds | int | `1` |  |
| test.enabled | bool | `true` |  |
| tolerations | list | `[]` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.13.1](https://github.com/norwoodj/helm-docs/releases/v1.13.1)
