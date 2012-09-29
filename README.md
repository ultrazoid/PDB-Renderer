PDB-Renderer
============

A Python based .pdb file renderer using pyOpenGL<br>
This program is still in it's basic forms...<br><br>
All PDB files are found here: <a href="http://www.pdb.org">Protein Data Bank</a><br>
Documentation for PDB files can be found here: <a href="http://www.wwpdb.org/documentation/format33/v3.3.html">Atomic Coordinate Entry Format Description</a><br>
And, Documentation on the OpenGL Coordinates can be found here: <a href="http://www.wwpdb.org/documentation/format33/sect9.html#ATOM">Coordinate Section: ATOM</a>

<h2>DONE:</h2>
<ul>
<li>Read file in</li>
<li>Analyse file to find OpenGL Data</li>
<li>Move this to a new list for rendering</li>
<li>Sort through to find X,Y,Z Coords</li>
</ul>

<h2>TO-DO:</h2>
<ul>
<li>Make small spheres (.025,5,5) at these locations</li>
<li>change colours depending on atom type</li>
<li>allow user to move around rendered structure</li>
<li>change cursor to show orbitting capability</li>
</ul>