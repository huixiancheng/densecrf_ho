#!/usr/bin/env python
import csv
import sys
import os


def main():
    if len(sys.argv) < 2:
        print "Missing argument:"
        print "accuracy.py /path/to/results/folder/"
        return 1
    path_to_folder = sys.argv[1]

    with open(os.path.join(path_to_folder, 'conf_mat.csv'), 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        all_values = []
        for row in csv_reader:
            all_values.append([int(elt) for elt in row])

    nb_of_correct_pixels = 0
    nb_of_total_pixels = 0

    for i, row in enumerate(all_values):
        for j, elt in enumerate(row):
            # Should we ignore the last "no classification" row???
            if j == len(row) - 1:
                continue
            nb_of_total_pixels += elt
            if i == j:
                nb_of_correct_pixels += elt

    print "Nb of correct pixels: " + str(nb_of_correct_pixels)
    print "Nb of total pixels: " + str(nb_of_total_pixels)
    print "Pixelwise accuracy: " + \
        str(100 * nb_of_correct_pixels / float(nb_of_total_pixels)) + \
        "%\n\n"

    cls_accuracies = []
    # Should we ignore the last "no classification" row???
    for cls in range(len(all_values[0]) - 1):
        correct = all_values[cls][cls]
        all_of_cls = sum(all_values[pred][cls]
                         for pred in range(len(all_values)))
        cls_accuracies.append(correct / float(all_of_cls))

    print "Global accuracy: " + str(sum(cls_accuracies) / len(cls_accuracies))

if __name__ == '__main__':
    sys.exit(main())
