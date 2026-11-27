"""Công cụ của bài toán — tra cứu đặt chỗ và chuyến bay thay thế từ dữ liệu giả.

Mỗi công cụ là một hàm Python gắn @tool, docstring ghi đủ 4 ý:
tên · input · output · có tác động ra ngoài không.
"""
import json
import os

from tracing import tool, TOOLS  # noqa: F401

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DATA_PATH = os.path.join(_ROOT, "data", "flights.json")


def _load_data() -> dict:
    with open(_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def _classify_flights(
    flights: list,
    so_khach: int,
    gio_den_toi_da: str = None,
    gio_di_toi_thieu: str = None,
) -> dict:
    hop_le = []
    da_huy = []
    thieu_du_lieu_ghe = []
    thieu_ghe = []
    den_muon_hoac_khac_gio = []

    for flight in flights:
        item = dict(flight)
        if item.get("trang_thai") == "huy":
            da_huy.append(item)
            continue

        con_ghe = item.get("con_ghe")
        if con_ghe is None:
            thieu_du_lieu_ghe.append(item)
            continue

        if con_ghe < so_khach:
            thieu_ghe.append(item)
            continue

        gio_den = item.get("gio_den") or ""
        gio_di = item.get("gio_di") or ""
        if (gio_den_toi_da and gio_den > gio_den_toi_da) or (
            gio_di_toi_thieu and gio_di < gio_di_toi_thieu
        ):
            den_muon_hoac_khac_gio.append(item)
            continue

        hop_le.append(item)

    return {
        "hop_le": hop_le,
        "da_huy": da_huy,
        "thieu_du_lieu_ghe": thieu_du_lieu_ghe,
        "thieu_ghe": thieu_ghe,
        "den_muon_hoac_khac_gio": den_muon_hoac_khac_gio,
    }


@tool
def tra_dat_cho(ma_dat_cho: str) -> dict:
    """Tên: tra_dat_cho — Tra thông tin đặt chỗ và chuyến bay gốc trong data/flights.json.
    Input: ma_dat_cho (str), ví dụ 'TRV-7Q2K'.
    Output: dict gồm tim_thay, ma_dat_cho, ngay_tham_chieu, hanh_khach, tong_hanh_khach, so_nguoi_lon, so_tre_em, tuoi_tre_em, tre_di_mot_minh, chuyen_goc, ten_san_bay_di, ten_san_bay_den.
    Không tác động ra ngoài."""
    data = _load_data()
    ma = (ma_dat_cho or "").strip().upper()
    ref_date = data.get("ngay_tham_chieu", "")
    booking = (data.get("dat_cho") or {}).get(ma)
    if not booking:
        return {
            "tim_thay": False,
            "ma_dat_cho": ma,
            "ngay_tham_chieu": ref_date,
        }

    hanh_khach = list(booking.get("hanh_khach") or [])
    nguoi_lon = [p for p in hanh_khach if p.get("loai") == "nguoi_lon"]
    tre_em = [p for p in hanh_khach if p.get("loai") == "tre_em"]
    tuoi_tre_em = [p.get("tuoi") for p in tre_em if p.get("tuoi") is not None]

    ma_chuyen_goc = booking.get("chuyen_goc", "")
    chuyen_goc = None
    for flight in data.get("chuyen_bay") or []:
        if flight.get("ma") == ma_chuyen_goc:
            chuyen_goc = dict(flight)
            break

    san_bay = data.get("san_bay") or {}
    di = (chuyen_goc or {}).get("di", "")
    den = (chuyen_goc or {}).get("den", "")

    return {
        "tim_thay": True,
        "ma_dat_cho": ma,
        "ngay_tham_chieu": ref_date,
        "hanh_khach": hanh_khach,
        "tong_hanh_khach": len(hanh_khach),
        "so_nguoi_lon": len(nguoi_lon),
        "so_tre_em": len(tre_em),
        "tuoi_tre_em": tuoi_tre_em,
        "tre_di_mot_minh": bool(booking.get("tre_di_mot_minh", False)),
        "chuyen_goc": chuyen_goc,
        "ten_san_bay_di": san_bay.get(di, di),
        "ten_san_bay_den": san_bay.get(den, den),
    }


@tool
def tra_chuyen_thay_the(
    di: str,
    den: str,
    ngay: str = None,
    so_khach: int = 1,
    gio_den_toi_da: str = None,
    gio_di_toi_thieu: str = None,
    bo_qua_ma: str = None,
) -> dict:
    """Tên: tra_chuyen_thay_the — Tra và phân loại chuyến bay thay thế trên chặng từ data/flights.json.
    Input: di (str), den (str), ngay (str | None, 'YYYY-MM-DD'), so_khach (int), gio_den_toi_da (str | None, 'HH:MM'), gio_di_toi_thieu (str | None, 'HH:MM'), bo_qua_ma (str | None).
    Output: dict phân loại các chuyến (hop_le, da_huy, thieu_du_lieu_ghe, thieu_ghe, den_muon_hoac_khac_gio, ngay_khac_hop_le, san_bay_khac) cùng thông tin sân bay. Giữ nguyên con_ghe = None khi thiếu dữ liệu.
    Không tác động ra ngoài."""
    data = _load_data()
    ref_date = data.get("ngay_tham_chieu", "")
    di_u = (di or "").strip().upper()
    den_u = (den or "").strip().upper()
    skip_code = (bo_qua_ma or "").strip().upper()
    san_bay = data.get("san_bay") or {}
    all_flights = data.get("chuyen_bay") or []

    route_flights = [
        dict(f)
        for f in all_flights
        if f.get("di") == di_u
        and f.get("den") == den_u
        and f.get("ma") != skip_code
        and (not ref_date or (f.get("ngay") or "") >= ref_date)
    ]
    route_flights.sort(key=lambda f: (f.get("ngay") or "", f.get("gio_di") or ""))

    if ngay:
        target_flights = [f for f in route_flights if f.get("ngay") == ngay]
        classified = _classify_flights(
            target_flights, so_khach, gio_den_toi_da, gio_di_toi_thieu
        )
        ngay_khac_hop_le = [
            dict(f)
            for f in route_flights
            if (f.get("ngay") or "") > ngay
            and f.get("trang_thai") != "huy"
            and f.get("con_ghe") is not None
            and f.get("con_ghe") >= so_khach
        ]
    else:
        classified = _classify_flights(
            route_flights, so_khach, gio_den_toi_da, gio_di_toi_thieu
        )
        ngay_khac_hop_le = []

    san_bay_khac = []
    for f in all_flights:
        if (
            f.get("di") == di_u
            and f.get("den") != den_u
            and f.get("ma") != skip_code
            and f.get("trang_thai") != "huy"
            and f.get("con_ghe") is not None
            and f.get("con_ghe") >= so_khach
        ):
            f_ngay = f.get("ngay") or ""
            if (ngay and f_ngay == ngay) or (not ngay and (not ref_date or f_ngay >= ref_date)):
                alt = dict(f)
                alt["ten_san_bay_den"] = san_bay.get(alt.get("den", ""), alt.get("den", ""))
                alt["khac_san_bay_den"] = True
                san_bay_khac.append(alt)
    san_bay_khac.sort(key=lambda f: (f.get("ngay") or "", f.get("gio_di") or ""))

    return {
        "di": di_u,
        "den": den_u,
        "ten_san_bay_di": san_bay.get(di_u, di_u),
        "ten_san_bay_den": san_bay.get(den_u, den_u),
        "ngay": ngay,
        "ngay_tham_chieu": ref_date,
        "so_khach": so_khach,
        "gio_den_toi_da": gio_den_toi_da,
        "gio_di_toi_thieu": gio_di_toi_thieu,
        **classified,
        "ngay_khac_hop_le": ngay_khac_hop_le,
        "san_bay_khac": san_bay_khac,
    }
