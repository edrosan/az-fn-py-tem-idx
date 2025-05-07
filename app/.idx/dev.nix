# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.azure-cli
    pkgs.azure-functions-core-tools
  ];
  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "humao.rest-client"
      "ms-azuretools.vscode-azurefunctions"
      "ms-azuretools.vscode-azureresourcegroups"
      "ms-python.autopep8"
      "ms-python.debugpy"
      "ms-python.python"
      "PKief.material-icon-theme"
    ];
    # Enable previews
    previews = {
      enable = true;
      previews = {
        # web = {
        #   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
        #   # and show it in IDX's web preview panel
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
        #   env = {
        #     # Environment variables to set for your server
        #     PORT = "$PORT";
        #   };
        # };
      };
    };
    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Example: install JS dependencies from NPM
        create-venv = "[ -d $PWD/.venv ] || python -m venv $PWD/.venv";
        test-hook = "echo 'onCreate hook running' > oncreate.log";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [];
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Example: start a background task to watch and re-build backend code
        # watch-backend = "npm run watch-backend";
      };
    };
  };
  # services = {
  #   docker = {
  #     enable = true;
  #   };
  # };
}
