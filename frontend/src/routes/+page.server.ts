import type { Actions } from '@sveltejs/kit';
import { fail } from '@sveltejs/kit';
import axios from 'axios';
import { COOKIE_API_KEY } from '$env/static/private';

export const actions = {
	default: async ({request, }) => {
		const form_data = await request.formData();

		const num_cookies = Number(form_data.get('num_cookies')?.toString());
		const cookie_diameter = Number(form_data.get('cookie_diameter')?.toString());
		const tray_width = Number(form_data.get('tray_width')?.toString());
		const tray_length = Number(form_data.get('tray_length')?.toString());

		if (!num_cookies || !cookie_diameter || !tray_width || !tray_length) {
			return fail(400, {num_cookies, cookie_diameter, tray_width, tray_length, missing: true});
		}

		if (cookie_diameter > tray_width || cookie_diameter > tray_length) {
			return fail(400, {num_cookies, cookie_diameter, tray_width, tray_length, tooLarge: true});
		}

		let res = await axios.post(
			'http://127.0.0.1:5000/optimize',
			form_data,
			{
				headers: {
					'x-api-key': COOKIE_API_KEY,
					"Content-Type": "application/json"
				}
			}
		)

		if (res.status !== 200) {
			return fail(500, {api_data: res.data});
		}
		return {success: true, data: res.data};
	}
} satisfies Actions