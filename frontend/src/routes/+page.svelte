<script lang="ts">
	import { enhance } from '$app/forms';
	import { goto } from '$app/navigation';
    import type { ActionData } from './$types';

    let { form }: { form: ActionData } = $props();
    if (form?.success) {
        goto('/results');
    }
</script>

<div>
    <!--header-->
    <div class='flex items-center flex-col mt-24'>
        <div class='w-48 mb-4'>
            <img class='object-contain' alt='bitten-cookie' src='/bitten-cookie.svg'/>
        </div>
        <div class='text-center'>
            <h1 class='text-2xl/7 font-bold text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight mb-4'>Cookies!</h1>
            <p>Don't know how to position cookies in a tray without them touching each other?</p>
            <p>Just fill out the form, we will tell you exactly where to put them!</p>
        </div>
    </div>
    <!--form-->
    <div class='cookie-form'>
        <form method='get' action='/results'  class='flex flex-col items-center' use:enhance>
            <div class='grid grid-cols-2 gap-x-4'>
                <input placeholder="Number of cookies" class='w-48 mb-4' type='number' name='num_cookies' value={form?.num_cookies ?? ''} required/>
                <input placeholder="Expected diameter of each cookie (cm)" class='w-48 mb-4' type='number' name='cookie_diameter' value={form?.cookie_diameter ?? ''} required/>
                <input placeholder="Tray width (cm)" class='w-48 mb-4' type='number' name='tray_width' value={form?.tray_width ?? ''} required/>
                <input placeholder="Tray length (cm)" class='w-48 mb-4' type='number' name='tray_length' value={form?.tray_length ?? ''} required/>
            </div>
            <button type='submit'>Submit</button>
        </form>
    </div>
</div>