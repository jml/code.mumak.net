{ stdenv, pkgs, fetchFromGitHub }:
let
  plugins = fetchFromGitHub {
    owner = "jml";
    repo = "pelican-plugins";
    rev = "master";
    sha256 = "0k9gpglpm6dqyd5w6896qph4ahkrs9189i9z88pkh5r7fic4q92k";
  };
  themes = fetchFromGitHub {
    owner = "jml";
    repo = "pelican-themes";
    rev = "jml-tweaks";
    sha256 = "0bld7rxahqpv9fn61i4a8g17qk5mmwin66c0yri0d02pck4cd3h7";
  };

  pelican = pkgs.lib.overrideDerivation pkgs.pythonPackages.pelican (oldAttrs: {
    doCheck = false;
    doInstallCheck = false;
  });

  pelican-alias = pkgs.buildPythonPackage (rec {
    name = "pelican-alias-${version}";
    version = "1.1";

    src = pkgs.fetchurl {
      url = "https://pypi.python.org/packages/af/0a/82422526f2d69917015ed7d47ba6dcd2789875359595fc5cb04a58115ec9/${name}.tar.gz";
      sha256 = "e548c8245127bd540d53d9b1a95c8fb6958184f819d13f996f208f45f7237c4f";
    };

    propagatedBuildInputs = [ pelican ];

    meta = {
      description = ''
        Pelican plugin for creating alias pages (useful for moving from a
        different URL scheme such as /<year>/<month>/<title>/ as used by
        Wordpress).
      '';
      homepage = "http://github.com/Nitron/pelican-alias";
      license = "MIT";
    };
  });
in
pkgs.buildPythonPackage {
  name = "code.mumak.net";
  version = "latest";

  src = ./.;

  propagatedBuildInputs = with pkgs.pythonPackages; [
    pelican
    ghp-import
    markdown
    pelican-alias
    typogrify
    pkgs.s3cmd

    # These need to be available at runtime.
    pexpect
    decorator
    simplegeneric
  ];

  shellHook = ''
    [ -h plugins ] && rm plugins
    if [ -e plugins ]; then
      echo "plugins exists and is not a symlink. Leaving unchanged."
    else
      ln -s ${plugins} plugins
    fi

    [ -h themes ] && rm themes
    if [ -e themes ]; then
      echo "themes exists and is not a symlink. Leaving unchanged."
    else
      ln -s ${themes} themes
    fi
  '';
}
