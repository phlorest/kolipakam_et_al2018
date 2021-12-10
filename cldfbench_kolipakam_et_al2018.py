import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "kolipakam_et_al2018"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'rsos171504supp5.trees', detranslate=True),
            self.metadata,
            args.log)
        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('drav_cov_est_ucln_yule_no_burnin.trees.gz'),
                1000),
            detranslate=True,
            as_nexus=True)

        args.writer.add_posterior(
            posterior.trees.trees, 
            self.metadata, 
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('drav.nex'),
            self.characters, 
            args.log)
