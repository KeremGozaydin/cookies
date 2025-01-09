import type { Config } from 'tailwindcss';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
		  colors: {
			cookie: {
			  brown: '#C87941',
			  beige: '#F2D2B6',
			  chocolate: '#3B240B',
			  white: '#FFF9F0',
			  golden: '#BA8448',
			  deep: '#8B4513',
			},
		  },
		  backgroundImage: {
			"cookie-gradient": 'linear-gradient(90deg, #C87941 0%, #F2D2B6 50%, #C87941 100%)',
		  }		
		},
	  },

	plugins: []
} satisfies Config;
