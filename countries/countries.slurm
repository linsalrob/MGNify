#!/bin/bash
#SBATCH --job-nameMGNify_countries
#SBATCH --time=1-0
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH -o countries-%j.out
#SBATCH -e countries-%j.err

set -euo pipefail
eval "$(conda shell.bash hook)"
conda activate bioinfie

python ../examples/countries.py -p 10000 -v

