#!/bin/bash

# Install Oh My Zsh
echo "Installing Oh My Zsh..."
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install Terminator
echo "Installing Terminator..."
sudo apt-get update
sudo apt-get install terminator

# Configure Terminator with four split panes
echo "Configuring Terminator..."
cat << EOF > ~/.config/terminator/config
[global_config]
  title_transmit_bg_color = "#d30102"
  title_transmit_fg_color = "#ffffff"
[keybindings]
[layouts]
  [[default]]
    [[[child0]]]
      type = Terminal
      parent = window0
      profile = default
    [[[child1]]]
      type = Terminal
      parent = window0
      profile = default
    [[[child2]]]
      type = Terminal
      parent = window0
      profile = default
    [[[child3]]]
      type = Terminal
      parent = window0
      profile = default
    [[[window0]]]
      type = Window
      parent = ""
      size = 1920, 1080
[plugins]
EOF

echo
