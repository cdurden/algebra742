mkdir -p build
i=1
cat Expressions | while read exprs; do
  exprA=`echo ${exprs} | awk '{print $1}'`
  exprB=`echo ${exprs} | awk '{print $2}'`
#  echo ${exprs}
  #echo ${exprA}
  #echo ${exprB}
  sed -e "s/{expr}/${exprA}/" template.tex > build/expr${i}a.tex
  sed -e "s/{expr}/${exprB}/" template.tex > build/expr${i}b.tex
  i=$((i+1))
done
cd build
for file in `ls -1 *.tex`; do
  pdflatex -shell-escape ${file}
done
