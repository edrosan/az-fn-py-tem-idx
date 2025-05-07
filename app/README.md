# Proyecto: Entorno de Desarrollo con Nix
<img alt="PyPI - PyJWT" src="https://img.shields.io/pypi/v/PyJWT.svg">

Este proyecto utiliza [Nix](https://nixos.org/) para definir y gestionar un entorno de desarrollo reproducible, ideal para equipos que requieren consistencia en las herramientas y dependencias.

## Características principales

- **Canal Nixpkgs:** Se utiliza el canal `stable-24.05` para garantizar estabilidad en los paquetes.
- **Paquetes incluidos:**
  - Python 3.11 (`python311`)
  - Pip para Python 3.11 (`python311Packages.pip`)
  - Azure CLI (`azure-cli`)
  - Azure Functions Core Tools (`azure-functions-core-tools`)
- **Variables de entorno:** Puedes definir variables personalizadas en la sección `env`.
- **Extensiones recomendadas para VS Code/IDX:**
  - humao.rest-client
  - ms-azuretools.vscode-azurefunctions
  - ms-azuretools.vscode-azureresourcegroups
  - ms-python.autopep8
  - ms-python.debugpy
  - ms-python.python
  - PKief.material-icon-theme

## Automatizaciones

- **onCreate:** Al crear el workspace, se genera automáticamente un entorno virtual de Python (`.venv`) si no existe.
- **Previews:** El sistema está preparado para habilitar vistas previas web, solo necesitas descomentar y ajustar la configuración según tu proyecto.

## Personalización

- Puedes agregar más paquetes de Nix desde [search.nixos.org/packages](https://search.nixos.org/packages).
- Para agregar más extensiones de VS Code, consulta [open-vsx.org](https://open-vsx.org/).
- Puedes definir hooks adicionales para automatizar tareas al iniciar o crear el workspace.

## Recursos

- [Documentación de Nix](https://nixos.org/manual/nix/stable/)
- [Personalización de workspaces en Firebase/IDX](https://firebase.google.com/docs/studio/customize-workspace)

---

> Este archivo describe la configuración base del entorno. Modifica y amplía según las necesidades específicas de tu proyecto.
