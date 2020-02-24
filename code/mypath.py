class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'coco':
            return 'dataloaders/datasets/coco_dataset/'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
