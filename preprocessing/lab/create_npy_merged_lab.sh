for f1 in ../lab/bbox_fl_txt/*/; do
	f1="$(basename $f1)"
	echo $f1
	for i in {0..59}; do
		python3 /usr/share/metavision/sdk/ml/python_samples/bbox_txt2npy/fl_bbox_txt2npy.py -i ../lab/bbox_fl_txt/$f1/${f1}_${i}.txt -o ../lab/fl_bb_npy/$f1/${f1}_${i}_bbox.npy;
	done
done
