# Read from the file file.txt and print its transposed content to stdout.
awk '{for (i=1; i<=NF; i++) {a[i,NR]=$i}} END {for (i=1; i<=NF; i++) {for (j=1; j<=NR; j++) {printf a[i,j]; if (j<NR) printf " "} printf "\n"}}' file.txt

# i didnt write this because i suck
# but missing 1 question in bash looks dumb