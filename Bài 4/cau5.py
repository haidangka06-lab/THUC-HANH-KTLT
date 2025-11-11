def sort_list(lst):
    """Tra ve danh sach da sap xep(tang dan)."""
    return sorted(lst)
def find_min_max(lst):
    """Tra ve (min_value, max_value) cua lst"""
    if not lst:
        raise ValueError("Danh sach rong")
    return min(lst), max(lst)    
    
