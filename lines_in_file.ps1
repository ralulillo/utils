[int]$LinesInFile = 0
$reader = New-Object IO.StreamReader 'data_20171117_20171123.csv'
while($reader.ReadLine() -ne $null){ $LinesInFile++ }
