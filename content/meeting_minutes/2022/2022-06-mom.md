Title: April Meet Minutes
Date: 2022-06-06 00:00
Tags: Monday-Modules

Introduction:
It's always hard to parse the binary file to text. Today we will see rescue module which will help us to convert docx to md file.

Module: docx2md

Installation: pip install docx2md

About:
Converts Microsoft Word document files (.docx extension) to Markdown files.

Execution:
% python -m docx2md ~/Downloads/example.docx output.msd 
	# save output.msd
	# save media/image1.png
	# save media/image4.jpg
	# save media/image3.gif
	# save media/image2.png


Output:
% cat output.msd 
	<div class="break"></div>

	# chapter 1

	text of chapter 1

	## section 1-1

	text of section 1-1

	### subsection 1-1-1

	text of subsection 1-1-1

	<div class="break"></div>

	insert png

	<img src="media/image1.png" id="image1">

	insert bmp

	<img src="media/image2.png" id="image2">

	insert gif

	<img src="media/image3.gif" id="image3">

	insert jpg

	<img src="media/image4.jpg" id="image4">

	<div class="break"></div>

	* aaaaa
	* bbbbb
	* ccccc

	* ddddd
	    * eeeee
		* fffff
		    * ggggg
		* hhhhh
	    * iiiii
	* jjjjj

	<table id="table1">
	<tr>
	<td>a</td>
	<td>b</td>
	<td>c</td>
	</tr>
	<tr>
	<td>d</td>
	<td>e</td>
	<td>f</td>
	</tr>
	<tr>
	<td>g</td>
	<td>h</td>
	<td>i</td>
	</tr>
	</table>


Reference:
https://pypi.org/project/docx2md/
