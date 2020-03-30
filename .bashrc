export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# Enable shims and autocompletion for pyenv.
eval "$(pyenv init -)"
# Load pyenv-virtualenv automatically by adding
# # the following to ~/.zshrc:
#
eval "$(pyenv virtualenv-init -)"
