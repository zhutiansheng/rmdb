use Bio::DB::Fasta;
#这一列就不用解释了吧，引用Bio::DB::Fasta模块

  # create database from directory of fasta files
  my $db      = Bio::DB::Fasta->new('all.con');
my $obj     = $db->get_Seq_by_id('CHROMOSOME_I');
my $length  = $obj->length;
print $length;

