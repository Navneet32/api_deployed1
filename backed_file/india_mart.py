import requests
from urllib.parse import urlencode

def search_indiamart(query, city, pages=1):
    cookies = {
        '_gcl_au': '1.1.298571876.1746780927',
        '_ga': 'GA1.1.736334251.1746780927',
        '__gsas': 'ID=8d91147e41a267a8:T=1746780940:RT=1746780940:S=ALNI_MbzamiV3_KgH8CXMWm__4BN3ErG6g',
        '_ym_uid': '1746780949675296447',
        '_ym_d': '1746780949',
        'G_ENABLED_IDPS': 'google',
        'pop_mthd': 'FL%3D0%7CDTy%3D1',
        'iploc': 'gcniso%3DIN%7Cgcnnm%3DIndia%7Cgctnm%3DAhmedabad%7Cgctid%3D70472%7Cgacrcy%3D10%7Cgip%3D43.241.144.149%7Cgstnm%3DGujarat',
        '_ym_isad': '2',
        'sessid': 'spv=1',
        '__gads': 'ID=a8cf23df7a2d8a34:T=1746780940:RT=1747033194:S=ALNI_Ma9ZDgvZCQuQVi-6FzMh_EABCChYw',
        '__gpi': 'UID=000010b9dd00bdae:T=1746780940:RT=1747033194:S=ALNI_MaSCRKHWUxFBYKZ_Gxpr8abiQbFqQ',
        '__eoi': 'ID=a7d42e3712934b06:T=1746780940:RT=1747033194:S=AA-AfjakiMB0qV9VwvAKM39Ousi-',
        'r': 'g',
        '_clck': '1he0snq%7C2%7Cfvu%7C0%7C1958',
        '_ym_visorc': 'b',
        'hd_ctval': f'ctval%3D{city}',
        'site-entry-page': 'https://www.indiamart.com/proddetail/diamond-necklace-set-2854156221248.html?pos=2&kwd=jewellery&tags=A||||8230.883|Price|product|||SSnp|rsf:gd-|-res:RC5|ktp:N0|mtp:G|prpfl:1|wc:1|qr_nm:gd|cs:13435|com-cf:nl|ptrs:na|mc:409|cat:614|qry_typ:P|lang:en|flavl:10|rtn:0-0-0-0-1-9-0|qrd:250505|mrd:250505|prdt:250507|msf:hs|v=4|r=4',
        'FCNEC': '%5B%5B%22AKsRol8RpCBW2XdpMaZ6WWNH_Jv-X7vJKL2RosUNPRdqYa2Yw-ZBoAFwtaj6p0I8ny3YaaysemIyt_9a_IS7Atd46PH0dk_JmI2s2lel3bZimNxopky_CDk8MzTgdGlx9w8cxoZS9WQjPgwEGZSDdupxnkwNBK9VEg%3D%3D%22%5D%5D',
        'inactive_open': '1',
        'LGNSTR': '0%2C0%2C0%2C0%2C0%2C1%2C0%2C0',
        'ImeshVisitor': 'fn%3D%7Cem%3D%7Cphcc%3D91%7Ciso%3DIN%7Cmb1%3D8102042061%7Cpct%3D%7Cctid%3D%7Cglid%3D245825395%7Ccd%3D12%2FMAY%2F2025%7Ccmid%3D%7Cutyp%3DN%7Cpwl%3D%7Cev%3D%7Cuv%3DV%7Custs%3D%7Cadmln%3D0%7Cadmsales%3D0%7CsessionKey%3D66f74389-75ee-4c9d-a4aa-9937853f91d7',
        'im_iss': 't%3DeyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYifQ.eyJpc3MiOiJVU0VSIiwiYXVkIjoiOCowKjAqMio2KiIsImV4cCI6MTc0NzExOTg2MCwiaWF0IjoxNzQ3MDMzNDYwLCJzdWIiOiIyNDU4MjUzOTUiLCJjZHQiOiIxMi0wNS0yMDI1In0.i6CueRCcXaG6TkI5Y7LB5DRzAfxuHTyQZvGriJAQ2FE',
        'xnHist': f'pv%3D6%7Cipv%3D0%7Cfpv%3D0%7Ccity%3D{city}%7Ccvstate%3D%7Cpopupshown%3Dundefined%7Cinstall%3Dundefined%7Css%3Dundefined%7Cmb%3Dundefined%7Ctm%3Dundefined%7Cage%3Dundefined%7Ccount%3D0%7Ctime%3DMon%20May%2012%202025%2012%3A34%3A05%20GMT+0530%20%28India%20Standard%20Time%29%7Cglid%3D245825395%7Cgname%3DNavneet%20Sinha%7Cgemail%3Dnavneetsinha32000@gmail.com%7CcityID%3Dundefined',
        '_ga_8B5NXMMZN3': 'GS2.1.s1747033180$o4$g1$t1747033458$j2$l0$h0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=1, i',
        # 'referer': 'https://dir.indiamart.com/search.mp?ss=jewellery&v=4&mcatid=&catid=&cq=ahmedabad&cq_src=city-search_5&crs=city-landing&tags=res:RC4|ktp:N0|mtp:G|wc:1|cq:ahmedabad|qr_nm:gl-gd|cs:13974|com-cf:nl|ptrs:na|mc:409|cat:614|qry_typ:P|lang:en|rtn:3-0-1-0-0-5-1|tyr:1|qrd:250512|mrd:250512|prdt:250512|msf:hs',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': '_gcl_au=1.1.298571876.1746780927; _ga=GA1.1.736334251.1746780927; __gsas=ID=8d91147e41a267a8:T=1746780940:RT=1746780940:S=ALNI_MbzamiV3_KgH8CXMWm__4BN3ErG6g; _ym_uid=1746780949675296447; _ym_d=1746780949; G_ENABLED_IDPS=google; pop_mthd=FL%3D0%7CDTy%3D1; iploc=gcniso%3DIN%7Cgcnnm%3DIndia%7Cgctnm%3DAhmedabad%7Cgctid%3D70472%7Cgacrcy%3D10%7Cgip%3D43.241.144.149%7Cgstnm%3DGujarat; _ym_isad=2; sessid=spv=1; __gads=ID=a8cf23df7a2d8a34:T=1746780940:RT=1747033194:S=ALNI_Ma9ZDgvZCQuQVi-6FzMh_EABCChYw; __gpi=UID=000010b9dd00bdae:T=1746780940:RT=1747033194:S=ALNI_MaSCRKHWUxFBYKZ_Gxpr8abiQbFqQ; __eoi=ID=a7d42e3712934b06:T=1746780940:RT=1747033194:S=AA-AfjakiMB0qV9VwvAKM39Ousi-; r=g; _clck=1he0snq%7C2%7Cfvu%7C0%7C1958; _ym_visorc=b; hd_ctval=ctval%3DAhmedabad; site-entry-page=https://www.indiamart.com/proddetail/diamond-necklace-set-2854156221248.html?pos=2&kwd=jewellery&tags=A||||8230.883|Price|product|||SSnp|rsf:gd-|-res:RC5|ktp:N0|mtp:G|prpfl:1|wc:1|qr_nm:gd|cs:13435|com-cf:nl|ptrs:na|mc:409|cat:614|qry_typ:P|lang:en|flavl:10|rtn:0-0-0-0-1-9-0|qrd:250505|mrd:250505|prdt:250507|msf:hs|v=4|r=4; FCNEC=%5B%5B%22AKsRol8RpCBW2XdpMaZ6WWNH_Jv-X7vJKL2RosUNPRdqYa2Yw-ZBoAFwtaj6p0I8ny3YaaysemIyt_9a_IS7Atd46PH0dk_JmI2s2lel3bZimNxopky_CDk8MzTgdGlx9w8cxoZS9WQjPgwEGZSDdupxnkwNBK9VEg%3D%3D%22%5D%5D; inactive_open=1; LGNSTR=0%2C0%2C0%2C0%2C0%2C1%2C0%2C0; ImeshVisitor=fn%3D%7Cem%3D%7Cphcc%3D91%7Ciso%3DIN%7Cmb1%3D8102042061%7Cpct%3D%7Cctid%3D%7Cglid%3D245825395%7Ccd%3D12%2FMAY%2F2025%7Ccmid%3D%7Cutyp%3DN%7Cpwl%3D%7Cev%3D%7Cuv%3DV%7Custs%3D%7Cadmln%3D0%7Cadmsales%3D0%7CsessionKey%3D66f74389-75ee-4c9d-a4aa-9937853f91d7; im_iss=t%3DeyJ0eXAiOiJKV1QiLCJhbGciOiJzaGEyNTYifQ.eyJpc3MiOiJVU0VSIiwiYXVkIjoiOCowKjAqMio2KiIsImV4cCI6MTc0NzExOTg2MCwiaWF0IjoxNzQ3MDMzNDYwLCJzdWIiOiIyNDU4MjUzOTUiLCJjZHQiOiIxMi0wNS0yMDI1In0.i6CueRCcXaG6TkI5Y7LB5DRzAfxuHTyQZvGriJAQ2FE; xnHist=pv%3D6%7Cipv%3D0%7Cfpv%3D0%7Ccity%3Dahmedabad%7Ccvstate%3D%7Cpopupshown%3Dundefined%7Cinstall%3Dundefined%7Css%3Dundefined%7Cmb%3Dundefined%7Ctm%3Dundefined%7Cage%3Dundefined%7Ccount%3D0%7Ctime%3DMon%20May%2012%202025%2012%3A34%3A05%20GMT+0530%20%28India%20Standard%20Time%29%7Cglid%3D245825395%7Cgname%3DNavneet%20Sinha%7Cgemail%3Dnavneetsinha32000@gmail.com%7CcityID%3Dundefined; _ga_8B5NXMMZN3=GS2.1.s1747033180$o4$g1$t1747033458$j2$l0$h0',
    }
    all_results = []

    for page in range(1, pages + 1):
        params = {
            'q': query,
            'page': f'{page}',
            'AK': cookies.get('im_iss', ''),
            'options.filters.city.data': city,
            'search_type': '',
            'glusrid': '245825395',
            'source': 'dir.search',
            'geo_country_info.geo_country_name': 'India',
            'geo_country_info.geo_country_code': 'IN',
            'implicit_info.for_country.type': 'India',
            'implicit_info.for_country.data': 'IN',
        }

        base_url = "https://dir.indiamart.com/api/search.rp"
        full_url = f"{base_url}?{urlencode(params)}"

        response = requests.get(full_url, headers=headers, cookies=cookies)

        if response.status_code == 200:
            try:
                data = response.json()
                for i in range(len(data.get("results", []))):
                    more_results = data['results'][i].get('more_results')
                    if more_results:
                        item = {
                            'name': more_results[0].get('title'),
                            'title_url': more_results[0].get('title_url'),
                            'phone_number': more_results[0].get('pns')
                        }
                        all_results.append(item)
            except Exception as e:
                return {"error": f"Error parsing page {page}: {str(e)}"}
        else:
            return {"error": f"Failed to fetch page {page}. Status: {response.status_code}"}

    return all_results