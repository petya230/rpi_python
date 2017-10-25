#!/bin/bash
for i in $(seq 1 2 40)
do
	wakeonlan d0:27:88:1e:44:9e
	wakeonlan D0:27:88:1E:44:9E
done
