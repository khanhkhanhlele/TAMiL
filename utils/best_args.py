
best_args = {
'seq-cifar10':   { 'tam': {200: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'pairwise_weight':0.1,
                                    'code_dim':64,
                                    'reg_weight':0.1,
                                    'ema_update_freq':0.05,
                                    'ema_alpha':0.999,
                                    'n_epochs': 50},
                              500: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.2,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'pairwise_weight': 0.1,
                                    'code_dim': 64,
                                    'reg_weight': 0.1,
                                    'ema_update_freq': 0.05,
                                    'ema_alpha': 0.999,
                                    'n_epochs': 50}}},
    'seq-cifar100': {'tam': {200: {'lr': 0.03,
                                     'minibatch_size': 32,
                                     'alpha': 0.1,
                                     'beta': 0.5,
                                     'batch_size': 32,
                                     'pairwise_weight': 0.1,
                                     'code_dim': 64,
                                     'reg_weight': 0.1,
                                     'ema_update_freq': 0.05,
                                     'ema_alpha': 0.999,
                                     'n_epochs': 50},
                               500: {'lr': 0.03,
                                     'minibatch_size': 32,
                                     'alpha': 0.2,
                                     'beta': 0.5,
                                     'batch_size': 32,
                                     'pairwise_weight': 0.1,
                                     'code_dim': 64,
                                     'reg_weight': 0.1,
                                     'ema_update_freq': 0.05,
                                     'ema_alpha': 0.999,
                                     'n_epochs': 50}}},
    'seq-tinyimg': {'tam': {200: {'lr': 0.05,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 1.0,
                                    'batch_size': 32,
                                  'pairwise_weight': 0.1,
                                  'code_dim': 64,
                                  'reg_weight': 0.1,
                                  'ema_update_freq': 0.05,
                                  'ema_alpha': 0.999,
                                    'n_epochs': 50},
                              500: {'lr': 0.05,
                                    'minibatch_size': 32,
                                    'alpha': 0.2,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'pairwise_weight': 0.1,
                                    'code_dim': 64,
                                    'reg_weight': 0.1,
                                    'ema_update_freq': 0.05,
                                    'ema_alpha': 0.999,
                                    'n_epochs': 50}}},
    'seq-core50': {'tam': {200: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.1,
                                    'beta': 1.0,
                                    'batch_size': 32,
                                    'pairwise_weight': 0.1,
                                    'code_dim': 64,
                                    'reg_weight': 0.1,
                                    'ema_update_freq': 0.05,
                                    'ema_alpha': 0.999,
                                    'n_epochs': 15},
                              500: {'lr': 0.03,
                                    'minibatch_size': 32,
                                    'alpha': 0.2,
                                    'beta': 0.5,
                                    'batch_size': 32,
                                    'pairwise_weight': 0.1,
                                    'code_dim': 64,
                                    'reg_weight': 0.1,
                                    'ema_update_freq': 0.05,
                                    'ema_alpha': 0.999,
                                    'n_epochs': 15}}}
}