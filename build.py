#! /usr/bin/env python

import hindkit as kit

def main():
    family = kit.Family(
        trademark='Hind Vadodara',
        script_name='Gujarati',
    )
    family.set_masters()
    family.set_styles()
    builder = kit.Project(
        family,
        options={
            "do_style_linking": True,
            "additional_unicode_range_bits": [1, 2],
            "use_os_2_version_4": True,
            "prefer_typo_metrics": True,
            "build_ttf": True,
        },
    )
    builder.build()


if __name__ == '__main__':
    main()