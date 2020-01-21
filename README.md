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
