#! /usr/bin/env python

import hindkit as kit

# - - -

family = kit.Family(
    trademark = 'Hind Vadodara',
    script = 'Gujarati',
    hide_script_name = True,
)

family.set_masters(
    modules = [
        # 'kerning',
        'mark_positioning',
        'mark_to_mark_positioning',
        'devanagari_matra_i_variants',
    ],
)

family.set_styles()

# - - -

builder = kit.Builder(family)

builder.fontrevision = '1.000'

builder.set_options([

    'prepare_styles',   # stage i
    'prepare_features', # stage ii
    'compile',          # stage iii

    'makeinstances', #!
    'checkoutlines', #!
    # 'autohint',      #!

    'do_style_linking',
    'use_os_2_version_4',
    'prefer_typo_metrics',
    'is_width_weight_slope_only',

])
from_to = '/Users/pratikgajjar/personal/hind-vadodara/masters'
builder.import_glyphs(from_masters=from_to, to_masters=from_to, save_to_masters=from_to)

# builder.generate_designspace()
# builder.generate_fmndb()

builder.build()
