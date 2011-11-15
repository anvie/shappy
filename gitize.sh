#!/usr/bin/env sh

git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"
git config --global alias.bu "commit --allow-empty -am \"bump update\""
git config --global alias.fixup "commit -am fixup"
git config --global alias.crp cherry-pick


