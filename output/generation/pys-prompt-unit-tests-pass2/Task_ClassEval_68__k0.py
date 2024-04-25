class PageUtil:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size

    def get_page(self, page_number):
        start_index = (page_number - 1) * self.page_size
        end_index = min(start_index + self.page_size, len(self.data))
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        total_items = len(self.data)
        total_pages = (total_items + self.page_size - 1) // self.page_size
        has_previous = page_number > 1
        has_next = page_number < total_pages
        data = self.get_page(page_number)
        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": total_pages,
            "total_items": total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": data
        }

    def search(self, keyword):
        results = [item for item in self.data if str(item).find(keyword) != -1]
        total_results = len(results)
        total_pages = 1 if total_results > 0 else 0
        return {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }
