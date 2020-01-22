# trello-json-parser
Refined parser for trello json export

originally found from here https://gist.github.com/gremau/290ab394c9bf2d6d03c18444ff60c225

modified to output story points powerups on trello
added another file to parse actions instead of cards

## Download
Open a terminal, run this:

    sudo curl https://github.com/harindrawisnu/trello-json-parser/blob/master/trelloparsecard.py -o trelloparsecard && sudo chmod +x trelloparsecard

or

    sudo curl https://github.com/harindrawisnu/trello-json-parser/blob/master/trelloparseaction.py -o trelloparseaction && sudo chmod +x trelloparsecard
    
## Usage
    $ trelloparse -h
    usage: tp [-h] input output

    positional arguments:
      input       JSON File from Trello
      output      File to output to

    optional arguments:
      -h, --help  show this help message and exit
      
### Example
    $ trelloparsecard yourtrellofile.json yourparsedcard.json
    $ trelloparseaction yourtrellofile.json yourparsedaction.json

## Working with elastic

A new file added tapnldj.py that stand for trello action parser new line delimited json. This file can be used to compose your trello json export into newline delimited json or ndjson which you can easily upload to elasticsearch through kibana dashboard and visualize your team progress and performances

### Example

To upload your data into elastic, first download the parser and parse your trello json file

    $ curl https://github.com/harindrawisnu/trello-json-parser/blob/master/tapnldj.py -o tapnldj && sudo chmod +x tapnldj
    $ tapnldj yourtrellofile.json yourelasticndjson.json
    
Then upload your output json file into elasticsearch through kibana by following this step :
1. Go to your kibana homepage, for example http://localhost:5601
2. Click the link "Upload data from logfile"
3. Upload the json file as the result of the parser
4. Check the data structure and press import
5. Wait for your data being indexed then you can create visualization with it
