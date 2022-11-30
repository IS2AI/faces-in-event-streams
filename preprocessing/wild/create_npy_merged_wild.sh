f1=03
for i in {0..4}; do
	python3 /usr/share/metavision/sdk/ml/python_samples/bbox_txt2npy/fl_bbox_txt2npy.py -i ../bbox_fl_txt/${f1}/${f1}_1${i}.txt -o ../npy/bbox_fl/wild/${f1}/${f1}_1${i}_bbox.npy;
done
