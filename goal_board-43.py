# === Stage 43: Добавь пагинацию длинных списков ===
# Project: GoalBoard
class Paginator:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
        self.total_pages = (len(items) + page_size - 1) // page_size

    def get_page(self, page_num):
        if page_num < 1:
            page_num = 1
        if page_num > self.total_pages:
            page_num = self.total_pages
        start = (page_num - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def get_page_info(self, page_num):
        current = self.get_page(page_num)
        return {
            'page': page_num,
            'total_pages': self.total_pages,
            'current_page': current,
            'has_next': page_num < self.total_pages,
            'has_prev': page_num > 1,
        }
