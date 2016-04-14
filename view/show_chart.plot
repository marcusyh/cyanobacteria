file='/tmp/eth100'; size=10000; plot file using ($1*size):10, file using ($1*size):4 with lines, file using ($1*size):8 with lines, file using ($1*size):9 with lines;
file='/tmp/eth40'; size=1; plot file using ($1*size):($5):($5*0.0002) with points pt 7 ps var;             


ysize=500; size=1; unset logscale; set grid xtics ytics mxtics mytics; set xtics 0.001;  set ytics ysize; file='/tmp/eth40'; plot file using ($1*size):($5):(0.5) with points pt 7 ps var;
ymax=500; size=1; unset logscale; set grid xtics ytics mxtics mytics; set xtics 0.001;  set ytics (ymax/50); file='/tmp/eth40'; plot file using ($1*size):($5<=ymax?$5:ymax):(0.5) with points pt 7 ps var;

unset logscale; set grid xtics ytics mxtics mytics; set xtics 0.001;  set ytics 10; file='/tmp/eth40'; size=1; plot file using ($1*size):($5<=500?$5:500):(0.5) with points pt 7 ps var;
unset logscale; set grid xtics ytics mxtics mytics; set xtics 0.001;  set ytics 1; file='/tmp/eth40'; size=1; plot file using ($1*size):($5<=50?$5:50):(0.5) with points pt 7 ps var;
unset logscale; set grid xtics ytics mxtics mytics; set xtics 0.001;  set ytics 0.05; file='/tmp/eth40'; size=1; plot file using ($1*size):($5<=1?$5:1):(0.5) with points pt 7 ps var;

unset ytics; set grid xtics ytics mxtics mytics; set logscale y; set xtics 0.001; set ytics;  file='/tmp/eth40'; size=1; plot file using ($1*size):($5>10?$5:10):($5 * 0.001) with points pt 7 ps var;


set grid xtics ytics mxtics mytics; file='/tmp/eth40'; size=1; plot file using ($1*size):($5>10?$5:10):(0.5) with points pt 7 ps var;


ymax=50000; pointsize=0.5; ysingle=ymax/50.0; unset logscale; set grid xtics ytics mxtics mytics; set xtics 0.001;  set ytics ysingle; file='/tmp/eth40'; size=1; plot file using ($1*size):($5<=ymax?$5:ymax):(pointsize=0.5?pointsize:$5*0.001) with points pt 7 ps var;
ymin=10; unset ytics; set grid xtics ytics mxtics mytics; set logscale y; set xtics 0.001; set ytics;  file='/tmp/eth40'; size=1; plot file using ($1*size):($5>ymin?$5:ymin):(0.5) with points pt 7 ps var;

ymin=10; ymax=50000; pointsize=0.001; file='/tmp/eth40'; size=1; 
if(ymin<0){
    ysingle=ymax/50.0; set xtics 0.001; set ytics ysingle; unset logscale; 
    set grid xtics ytics mxtics mytics; plot file using ($1*size):($5<=ymax?$5:ymax):($5<=ymax?(pointsize>0.5?pointsize:$5*pointsize):0) with points pt 7 ps var;
}else{
    unset ytics; set ytics; set logscale y; set xtics 0.001; 
    set grid xtics ytics mxtics mytics; plot file using ($1*size):($5>=ymin?$5:ymin):($5<=ymax?(pointsize>0.5?pointsize:$5*pointsize):0) with points pt 7 ps var;
}; 

ymin=10; ymax=50000; pointsize=0.6; file='/tmp/eth40'; size=1; if(ymin<0){ysingle=ymax/50.0; set xtics 0.001; unset logscale; set ytics ysingle;set grid xtics ytics mxtics mytics; plot file using ($1*size):($5<=ymax?$5:ymax):($5<=ymax?(pointsize>0.5?pointsize:$5*pointsize):0) with points pt 7 ps var; }else{unset ytics; unset mytics; set xtics 0.001; set grid xtics ytics mxtics mytics; set ytics; set logscale y; plot file using ($1*size):($5>=ymin?$5:ymin):($5>=ymin?(pointsize>0.5?pointsize:$5*pointsize):0) with points pt 7 ps var;};

file='/tmp/eth40'; size=1; plot file using ($1*size):10, file using ($1*size):4 with lines, file using ($1*size):8 with lines, file using ($1*size):9 with lines;
