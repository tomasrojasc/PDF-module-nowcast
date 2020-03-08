## PDF Module
This module is part of the NOWCAST proyect by [ESO](https://www.eso.org) that aims to do short-term-forecast of the [seeing](https://en.wikipedia.org/wiki/Astronomical_seeing) parameter in order to improve astronomical observations.

## Features
This module makes a pdf of all the time series and the correlations for a given year


## How to use
Basically the only thing you have to do is set up 
the required files in the folder ``data`` the files are the followings:

   * ``dicts_of_utdf.pickle``
   * ``final_df.correlations``
   * ``max_corr_df.correlations``
   * ``UTdf.all_days``

This files are produced by the other modules of the project

After all that is done, you have to execute the ``main.py`` file
## Things to note
All the intermediate files are deleted after the execution is done. This is to avoid confusions. This can be ignored by deleting the line in ``main.py`` that executes the ``clean.sh`` bash file.

## Credits
  * The ``scripts/merge4.py`` file was obtained from the demo scripts of the module
  ``pdfrw`` avaliable [here](https://github.com/pmaupin/pdfrw/blob/master/examples/4up.py)
