# Individual Project #1: Continuous Integration using GitHub Actions of Python Data Science Project


Requirements:
	
* The project structure must include the following files:	
    * Jupyter Notebook with:
	    * Cells that perform descriptive statistics using Polars or Panda.
		* Tested by using nbval plugin for pytest
			
    * Python Script performing the same descriptive statistics using Polars or Panda
    * lib.py file that shares the common code between the script and notebook
	* Makefile with the following:	
        * Run all tests (must test notebook and script and lib)			
        * Formats code with Python black
        * Lints code with Ruff
        * Installs code via:  pip install -r requirements.txt
		
* test_script.py to test script	
* test_lib.py to test library		
* Pinned requirements.txt
* GitHub Actions performs all four Makefile commands with badges for each one in the README.md
		
	
	
