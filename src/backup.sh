#!/bin/bash

cd /vagrant
backuptime=$(date +%m%d)
tar cvzf home.${backuptime}.tar.gz ~/.
