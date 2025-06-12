#!/usr/bin/env python3
import arxiv

def fetch_bibtex_with_lib(arxiv_id: str) -> str:
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id], max_results=1)
    result = next(client.results(search), None)
    if result is None:
        raise ValueError(f"未找到 arXiv ID 为 {arxiv_id} 的论文")

    # 1. 标题
    title = result.title.strip().replace('\n', ' ')
    # 2. 作者：取 Author 对象的 name 属性
    authors = " and ".join(author.name for author in result.authors)
    # 3. 年份
    year = result.published.year
    # 4. eprint 和主分类
    eprint = arxiv_id
    primary_class = result.primary_category

    # 5. 组装 BibTeX
    bib = (
        f"@misc{{{eprint},\n"
        f"  title={{{title}}},\n"
        f"  author={{{authors}}},\n"
        f"  year={{{year}}},\n"
        f"  eprint={{{eprint}}},\n"
        f"  archivePrefix={{arXiv}},\n"
        f"  primaryClass={{{primary_class}}},\n"
        f"  url={{https://arxiv.org/abs/{eprint}}}\n"
        f"}}"
    )
    return bib

if __name__ == "__main__":
    try:
        print(fetch_bibtex_with_lib("2506.06677"))
    except Exception as e:
        print(f"获取 BibTeX 失败：{e}")
