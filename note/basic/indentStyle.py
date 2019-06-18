def api():
  search_no = get_search_no()
  if not search_no:
    Logger.get().warn("search_no doesn't exist.")
    return None, "error"
  else:
    try:
      result = special_execute_something(search_no)
      return result, None
    except:
      Logger.get().exception("Oh my god!!!")