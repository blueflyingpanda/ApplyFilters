from filters_applier import FiltersApplier

if __name__ == '__main__':
    try:
        fa = FiltersApplier('settings.conf')
    except Exception as e:
        print('Something went wrong. Perhaps invalid config:', e)
        exit(1)
    try:
        fa.apply_filters_to_all()
    except Exception as e:
        print('Could not apply filters:', e)
        exit(1)
    print('filters applied!')