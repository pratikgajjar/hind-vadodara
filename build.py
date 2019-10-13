#! /usr/bin/env python

import hindkit as kit

# - - -

family = kit.Family(
    trademark = 'Hind Vadodara',
    script_name = 'Gujarati',
)
#
# family.set_masters(
#     [
#         ("100", -50),
#         ("500", 44),
#         ("900", 150),
#     ]
# )
family.set_masters()
family.set_styles()

# - - -

builder = kit.Project(family)
builder.build()
#
# builder.set_options([
#
#     'prepare_styles',   # stage i
#     'prepare_features', # stage ii
#     'compile',          # stage iii
#
#     'makeinstances', #!
#     'checkoutlines', #!
#     # 'autohint',      #!
#
#     'do_style_linking',
#     'use_os_2_version_4',
#     'prefer_typo_metrics',
#     'is_width_weight_slope_only',
#
# ])

# builder.generate_designspace()
# builder.generate_fmndb()

