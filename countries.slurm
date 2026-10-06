#!/bin/bash
#SBATCH --job-name=Countries
#SBATCH --time=5-0
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH -o countries-%j.out
#SBATCH -e countries-%j.err

set -euo pipefail
eval "$(conda shell.bash hook)"
conda activate bioinformatics

python examples/countries.py -v

