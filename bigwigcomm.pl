#!/usr/bin/perl -w
open myfile,"wigfilelist" or "die can not open file";
my $prefix="nohup ./wigToBigWig ../zz/";
while(my $line=<myfile>){
	chomp($line);
	my $l=length($line)-13;
	$postfix=substr($line,9,$l);
	my $comm="nohup ./wigToBigWig ../zz/$line rice.chrom.sizes ../backup/bigwig/$postfix\.bw &\n";
	print($comm)
#print("$postfix\n");
}
