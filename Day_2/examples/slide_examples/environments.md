```bash
conda env list

conda create --name <environment_name>

conda activate <environment_name>

conda install <pckg_1> <pckg_2>

conda deactivate

conda env remove --name <environment_name>
```

```r
# Works best if combined with a .Rproj

renv::status()

renv::init()

renv::activate()

renv::install("pckg_1")
renv::install("pckg_2")

renv::snapshot() # updates renv.lock file!

renv::dependencies()

renv::deactivate()
```