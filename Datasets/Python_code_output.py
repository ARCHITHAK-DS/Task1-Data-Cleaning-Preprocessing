Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: C:/Users/archi/Downloads/Python code for cleaning and prepocessing.py
Dataset Shape: (8790, 10)

Column Data Types:
show_id           str
type              str
title             str
director          str
country           str
date_added        str
release_year    int64
rating            str
duration          str
listed_in         str
dtype: object

Missing Values:
show_id         0
type            0
title           0
director        0
country         0
date_added      0
release_year    0
rating          0
duration        0
listed_in       0
dtype: int64

Columns renamed
Extra spaces removed
Null values treated
Missing rows populated

Duplicates Found: 0
Duplicates removed
Text standardized
Date cleaned
Duration column split
Genre column standardized
Data types converted
Unneeded columns dropped

Remaining Null Values:
show_id           0
type              0
title             0
director          0
country           0
date_added        0
release_year      0
rating            0
listed_in         0
year_added        0
month_added       0
duration_value    0
duration_unit     0
genre_count       0
dtype: int64

Final Dataset Shape:
(8790, 14)

Cleaning Completed Successfully!
