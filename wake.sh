#!/bin/bash
for i in $(seq 1 2 40)
do
	wakeonlan macid
done
