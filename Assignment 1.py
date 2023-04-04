
get_ipython().run_cell_magic('bash', '--bg --out output', 'cat gutenberg/1/6/6/1661/1661.txt | tail -21 | head -5\n')

get_ipython().run_cell_magic('bash', '--bg --out output', 'cat agora/Agora.csv | grep Drugs/Cannabis/Weed | wc -l\n')

get_ipython().run_cell_magic('bash', '', 'rm -rf a\nrm -rf d\nrm -rf j\nmkdir -p a/b/c d/e/f j/k/l\n')

get_ipython().run_cell_magic('bash', '--bg --out output', 'ls amazon-reviews -lhS | head -2 | tail -1\n')

get_ipython().run_cell_magic('bash', '--bg --out output', 'find millionsong/A -name *.h5 | sort\n')

get_ipython().run_cell_magic('bash', '--bg --out output', 'find census -type f -size +1000000c -ls |sort -nk7 | tr -d \\\\ | tr -s " " | cut -d " " -f 7,11-\n\n# find census -type f -size +1000000c -ls |sort -nk7|tr -d \\\\  | awk \'{print $7,$11, $12, $13}\'\n')

get_ipython().run_cell_magic('bash', '--bg --out output', 'grep "mentions" gdeltv2/masterfilelist.txt | grep -E "201902140[8][0-9][0-9][0-9]" | cut -d " " -f 3 | sort\n')

get_ipython().run_cell_magic('bash', '--bg --out output', 'cat movielens/20m/ml-20m/tags.csv | cut -d "," -f 3 | sort | uniq | wc -l\n\n# awk -F \',\' \'{print $3}\' movielens/20m/ml-20m/tags.csv | sort| uniq | wc -l\n')

get_ipython().system('rm -f pandemic-books.txt')

get_ipython().run_cell_magic('bash', '', 'grep -i "pandemic" book-crossing/BX-Books.csv | cut -d ";" -f 2 > pandemic-books.txt\n\n# grep -i "pandemic" book-crossing/BX-Books.csv | awk -F \';\' \'{print $2}\' > pandemic-books.txt\n')

