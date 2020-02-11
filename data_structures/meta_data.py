class MetaData:
    def __init__(self, prefix):
        # initialize the prefix variable
        self.prefix = prefix

        # open the meta data txt file
        filename = 'meta/{}.meta'.format(prefix)
        with open(filename, 'r') as fd:
            lines = fd.readlines()

            for ix in range(0, len(lines), 2):
                # get the comment and the corresponding value
                comment = lines[ix].strip()
                value = lines[ix + 1].strip()

                if comment == '# resolution in nm':
                    # separate into individual dimensions
                    samples = value.split('x')
                    # need to use 2, 1, and 0 here since the outward facing convention is x,y,z, not z, y, x
                    self.resolution = (float(samples[2]), float(samples[1]), float(samples[0]))
                elif comment == '# segmentation filename':
                    self.segmentation_filename = value

    def Resolution(self):
        return self.resolution

    def SegmentationFilename(self):
        return self.segmentation_filename.split()[0], self.segmentation_filename.split()[1]