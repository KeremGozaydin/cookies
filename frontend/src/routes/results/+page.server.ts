import axios from "axios";
import type { PageServerLoad } from "../$types";
import { COOKIE_API_KEY } from '$env/static/private';
import { fail } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ url }) => {
    let params = url.searchParams;

    const num_cookies = Number(params.get('num_cookies')?.toString());
    const cookie_diameter = Number(params.get('cookie_diameter')?.toString());
    const tray_width = Number(params.get('tray_width')?.toString());
    const tray_length = Number(params.get('tray_length')?.toString());

    if (!num_cookies || !cookie_diameter || !tray_width || !tray_length) {
        return fail(400, {num_cookies, cookie_diameter, tray_width, tray_length, missing: true});
    }

    if (cookie_diameter > tray_width || cookie_diameter > tray_length) {
        return fail(400, {num_cookies, cookie_diameter, tray_width, tray_length, tooLarge: true});
    }

    try {
        let res = await axios.post(
            'http://127.0.0.1:5000/optimize',
            {
                num_cookies,
                cookie_diameter,
                tray_width,
                tray_length
            },
            {
                headers: {
                    'x-api-key': COOKIE_API_KEY,
                    "Content-Type": "application/json"
                }
            }
        )
        return {
            status: "success",
            optimized_postitions: res.data
        };
    }
    catch (e) {
        return fail(500, {api_data: e});
    }
}