{ pkgs ? import <nixpkgs> {} }:

let
  pythonPackages = pkgs.python39Packages;
in
pkgs.mkShell {
  name = "am-backend";

  buildInputs = [
    pkgs.python39
    pythonPackages.virtualenv
  ];

  shellHook = ''
    # Create a virtual environment if it doesn't exist
    if [ ! -d .venv ]; then
      virtualenv .venv
    fi
    
    # Activate the virtual environment
    source .venv/bin/activate

    # Install dependencies if they are not installed
    if [ ! -f .venv/requirements_installed ]; then
      pip install fastapi uvicorn
      touch .venv/requirements_installed
    fi
  '';
}

