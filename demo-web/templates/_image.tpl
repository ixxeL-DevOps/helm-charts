{{/* vim: set filetype=mustache: */}}
{{/*
Return the proper backend image name
*/}}
{{- define "demo-web.image" -}}
{{ include "common.images.image" (dict "imageRoot" .Values.image "global" .Values.global.image "context" .) }}
{{- end -}}


{{/*
Return the proper image name
{{ include "common.images.image" ( dict "imageRoot" .Values.path.to.the.image "global" .Values.global ) }}
*/}}
{{- define "common.images.image" -}}
{{- $registryName := .imageRoot.registry -}}
{{- $repositoryName := .imageRoot.repository -}}
{{- $separator := ":" -}}
{{- $termination := default .context.Chart.AppVersion .imageRoot.tag | toString -}}
{{- if .global }}
    {{- if .global.registry }}
     {{- $registryName = .global.registry -}}
    {{- end -}}
{{- end -}}
{{- if .imageRoot.digest }}
    {{- $separator = "@" -}}
    {{- $termination = .imageRoot.digest | toString -}}
{{- end -}}
{{- if $registryName }}
    {{- printf "%s/%s%s%s" $registryName $repositoryName $separator $termination }}
{{- else -}}
    {{- printf "%s%s%s" $repositoryName $separator $termination }}
{{- end -}}
{{- end -}}